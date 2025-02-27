// src/routes/baseball/teams/+page.ts
export const load = async ({ fetch }) => {
  // Fetch all teams
  const resTeams = await fetch('/api/teams/');
  if (!resTeams.ok) {
    throw new Error('Failed to fetch teams');
  }
  const teams = await resTeams.json();

  // Fetch all players
  const resPlayers = await fetch('/api/players/');
  if (!resPlayers.ok) {
    throw new Error('Failed to fetch players');
  }
  const players = await resPlayers.json();

  // Merge players into their respective team objects
  const teamsWithPlayers = teams.map(team => {
    const teamPlayers = players.filter(player => {
      // Case 1: player.team is an object (nested) with a slug property
      if (player.team && typeof player.team === 'object') {
        return player.team.slug === team.slug;
      }
      // Case 2: player.team is a number (team id)
      return player.team === team.id;
    });
    return { ...team, players: teamPlayers };
  });

  return { teams: teamsWithPlayers };
};
