

export const load = async ({ fetch }) => {
  // Define the API endpoints for each model.
  const endpoints = [
    '/api/items/',
    '/api/teams/',
    '/api/games/',
    '/api/players/',

    //'/api/atbats/'
  ];

  // Fetch all endpoints concurrently.
  const responses = await Promise.all(
    endpoints.map(endpoint => fetch(endpoint))
  );

  // Check each response for errors.
  responses.forEach((res, index) => {
    if (!res.ok) {
      throw new Error(`Failed to fetch data from ${endpoints[index]}`);
    }
  });

  // Parse the JSON from each response.
  const [items, teams, games, players, stats, atbats] = await Promise.all(
    responses.map(res => res.json())
  );

  // Return the data so it's available in your Svelte component.
  return { items, teams, games, players, stats, atbats };
};