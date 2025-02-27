// src/routes/baseball/teams/[slug]/+page.ts
export const load = async ({ fetch, params }) => {
  const { slug } = params;
  const decodedSlug = decodeURIComponent(slug);

  // Fetch team details
  const resTeam = await fetch(`/api/teams/${decodedSlug}/`);
  if (!resTeam.ok) {
    throw new Error(`Failed to fetch details for team: ${decodedSlug}`);
  }
  const team = await resTeam.json();

  // Fetch players for this team using the nested API endpoint
  const resPlayers = await fetch(`/api/teams/${decodedSlug}/players/`);
  if (!resPlayers.ok) {
    throw new Error(`Failed to fetch players for team: ${decodedSlug}`);
  }
  const players = await resPlayers.json();

  // Return the team data so it is available in the page component
  return { team, players };
};

  