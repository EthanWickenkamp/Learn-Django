<script lang="ts">
    export let data;
  </script>
  
  <h1>Games</h1>
  {#if data.games && data.games.length > 0}
    <ul>
      {#each data.games as game}
        <li>
          {game.home_team.name} vs {game.away_team.name} on {game.game_date}
        </li>
      {/each}
    </ul>
  {:else}
    <p>No games available.</p>
  {/if}
  