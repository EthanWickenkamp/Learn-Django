<!-- src/routes/baseball/teams/[slug]/+page.svelte -->
<script lang="ts">
  // The `data`A prop is provided by the load function
  export let data;
</script>

<style>
  h1 {
    margin-bottom: 0.5rem;
  }
  section {
    margin-top: 2rem;
  }
  ul {
    list-style: none;
    padding-left: 0;
  }
  li {
    margin-bottom: 0.5rem;
    padding: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
</style>

<!-- Display team details -->
<h1>{data.team.name}</h1>


<!-- Display players -->
<section>
  <h2>Players</h2>
  {#if data.players && data.players.length > 0}
    <ul>
      {#each data.players as player}
        <li>{player.name}</li>
      {/each}
    </ul>
  {:else}
    <p>No players found for this team.</p>
  {/if}
</section>
