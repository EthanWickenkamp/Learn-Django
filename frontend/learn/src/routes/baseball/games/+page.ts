// src/routes/baseball/games/+page.ts
export const load = async ({ fetch }) => {
    const res = await fetch('/api/games/');
    if (!res.ok) {
      throw new Error('Failed to fetch games');
    }
    const games = await res.json();
    return { games };
  };
  