import { useCallback, useEffect, useState } from 'react';

const PATHS = {
  home: '/',
  calculator: '/calculator',
  library: '/library',
  about: '/about',
} as const;

export type Route = keyof typeof PATHS;

function normalizePath(path: string): string {
  return path.length > 1 && path.endsWith('/') ? path.slice(0, -1) : path;
}

function routeFromPath(path: string): Route {
  const normalized = normalizePath(path);
  const routes = Object.keys(PATHS) as Route[];
  return routes.find((route) => PATHS[route] === normalized) ?? 'home';
}

// Makes the address bar match what's actually rendered (e.g. a trailing
// slash or an unrecognized path falls back to Home — the URL should say so too).
function syncPathToRoute(route: Route) {
  const canonical = PATHS[route];
  if (window.location.pathname !== canonical) {
    window.history.replaceState(null, '', canonical);
  }
}

export function useRouter() {
  const [route, setRoute] = useState<Route>(() => routeFromPath(window.location.pathname));

  useEffect(() => {
    syncPathToRoute(routeFromPath(window.location.pathname));
    const onPopState = () => {
      const next = routeFromPath(window.location.pathname);
      syncPathToRoute(next);
      setRoute(next);
    };
    window.addEventListener('popstate', onPopState);
    return () => window.removeEventListener('popstate', onPopState);
  }, []);

  const navigate = useCallback((next: Route) => {
    const path = PATHS[next];
    if (window.location.pathname !== path) {
      window.history.pushState(null, '', path);
    }
    setRoute(next);
    window.scrollTo(0, 0);
  }, []);

  return { route, navigate };
}
