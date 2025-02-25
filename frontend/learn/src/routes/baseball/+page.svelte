<script lang="ts">
    import { goto } from '$app/navigation';
    // The `data` prop is provided by the load function.
    export let data;

    // Navigate to a hypothetical edit page for a given section.
    function editSection(section: string) {
      // For example, navigating to /dashboard/edit/items or /dashboard/edit/teams
      goto(`/dashboard/edit/${section}`);
    }
</script>
  


<style>
    h1 {
      text-align: center;
      margin-top: 2rem;
    }
    section {
      margin: 2rem 0;
      padding: 1rem;
      border: 1px solid #ddd;
      border-radius: 8px;
    }
    h2 {
      margin-bottom: 0.5rem;
      border-bottom: 1px solid #ccc;
      padding-bottom: 0.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    button {
      padding: 0.25rem 0.75rem;
      font-size: 0.9rem;
      border: none;
      background-color: #007acc;
      color: #fff;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #005fa3;
    }
    ul {
      list-style: none;
      padding-left: 0;
    }
    li {
      margin: 0.5rem 0;
      padding: 0.5rem;
      border: 1px solid #eee;
      border-radius: 4px;
    }
  </style>
  
  <h1>Dashboard</h1>
  
  <section>
    <h2>
      Items
      <button on:click={() => editSection('items')}>Edit Items</button>
    </h2>
    {#if data.items && data.items.length > 0}
      <ul>
        {#each data.items as item}
          <li>
            <strong>{item.name}</strong>: {item.description}
          </li>
        {/each}
      </ul>
    {:else}
      <p>No items available.</p>
    {/if}
  </section>
  
  <section>
    <h2>
      Teams
      <button on:click={() => editSection('teams')}>Edit Teams</button>
    </h2>
    {#if data.teams && data.teams.length > 0}
      <ul>
        {#each data.teams as team}
          <li>{team.name}</li>
        {/each}
      </ul>
    {:else}
      <p>No teams available.</p>
    {/if}
  </section>
  
  <section>
    <h2>
      Games
      <button on:click={() => editSection('games')}>Edit Games</button>
    </h2>
    {#if data.games && data.games.length > 0}
      <ul>
        {#each data.games as game}
          <li>
            {game.home_team?.name || 'TBD'} vs {game.away_team?.name || 'TBD'} on {game.game_date}
          </li>
        {/each}
      </ul>
    {:else}
      <p>No games available.</p>
    {/if}
  </section>
  
  <section>
    <h2>
      Players
      <button on:click={() => editSection('players')}>Edit Players</button>
    </h2>
    {#if data.players && data.players.length > 0}
      <ul>
        {#each data.players as player}
          <li>
            {player.name} {#if player.team}({player.team.name}){/if}
          </li>
        {/each}
      </ul>
    {:else}
      <p>No players available.</p>
    {/if}
  </section>
  
  <section>
    <h2>
      Stats
      <button on:click={() => editSection('stats')}>Edit Stats</button>
    </h2>
    {#if data.stats && data.stats.length > 0}
      <ul>
        {#each data.stats as stat}
          <li>
            {stat.player?.name} in Game {stat.game?.id}: Hits: {stat.hits}, Runs: {stat.runs}, RBIs: {stat.rbis}
          </li>
        {/each}
      </ul>
    {:else}
      <p>No stats available.</p>
    {/if}
  </section>
  
  <section>
    <h2>
      AtBats
      <button on:click={() => editSection('atbats')}>Edit AtBats</button>
    </h2>
    {#if data.atbats && data.atbats.length > 0}
      <ul>
        {#each data.atbats as atbat}
          <li>
            {atbat.player?.name} - {atbat.outcome} in inning {atbat.inning}
          </li>
        {/each}
      </ul>
    {:else}
      <p>No atbats available.</p>
    {/if}
  </section>