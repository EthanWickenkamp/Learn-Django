// src/routes/baseball/teams/+page.ts
export const load = async ({ fetch }) => {
    const res = await fetch('/api/teams/');
    if (!res.ok) {
      throw new Error('Failed to fetch teams');
    }
    const teams = await res.json();
    return { teams };
  };
  