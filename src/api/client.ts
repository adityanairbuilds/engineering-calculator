// Explicit override (e.g. a custom API host) wins. Otherwise: the Vite dev server proxies
// nothing, so local dev needs the standalone backend's absolute URL; a Vercel build serves
// frontend and backend from the same origin (see vercel.json rewrites), so relative works there.
const API_BASE =
  (import.meta.env.VITE_API_BASE_URL as string | undefined) ?? (import.meta.env.DEV ? 'http://localhost:8000' : '');

export class ApiError extends Error {}

/** Fetches `path` from the FastAPI backend and parses the JSON body, or throws an ApiError with the backend's own message. */
export async function apiRequest<T>(path: string, init?: RequestInit): Promise<T> {
  let res: Response;
  try {
    res = await fetch(`${API_BASE}${path}`, {
      ...init,
      headers: { 'Content-Type': 'application/json', ...init?.headers },
    });
  } catch {
    throw new ApiError('Could not reach the backend — is it running?');
  }

  if (!res.ok) {
    const body = await res.json().catch(() => null);
    // FastAPI's own errors give a plain string `detail`; its automatic request-
    // validation errors (422) give a list of objects instead — fall back rather
    // than showing "[object Object]" for those.
    const message = typeof body?.detail === 'string' ? body.detail : `Request failed (${res.status}).`;
    throw new ApiError(message);
  }

  return res.json() as Promise<T>;
}
