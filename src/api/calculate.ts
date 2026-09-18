import { apiRequest } from './client';

export async function calculate(formulaId: string, target: string, values: Record<string, number>): Promise<number> {
  const result = await apiRequest<{ value: number }>(`/api/calculate/${encodeURIComponent(formulaId)}`, {
    method: 'POST',
    body: JSON.stringify({ target, values }),
  });
  return result.value;
}
