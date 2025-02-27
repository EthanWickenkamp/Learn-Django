<!-- src/routes/baseball/teams/+page.svelte -->
<script lang="ts">
  export let data;
</script>

<h1>Teams</h1>

<div class="grid">
  {#each data.teams as team}
    <div class="team-box">
      <div class="team-header">
        <a href={`/baseball/teams/${encodeURIComponent(team.slug)}`}>{team.name}</a>
      </div>
      <div class="team-content">
        <p><strong>Record:</strong> {team.record ? team.record : "N/A"}</p>
        <p><strong>Players:</strong>
          {#if team.players && team.players.length > 0}
            {team.players.map(player => player.name).join(', ')}
          {:else}
            No players
          {/if}
        </p>
      </div>
    </div>
  {/each}
</div>

<style>
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
  }
  .team-box {
    border: 1px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    background: #fff;
  }
  .team-header {
    background-color: #007BFF;
    color: white;
    padding: 0.5rem;
    font-weight: bold;
    text-align: center;
  }
  .team-content {
    padding: 1rem;
    font-size: 0.9rem;
    line-height: 1.4;
  }
  .team-content p {
    margin: 0.5rem 0;
  }
  .team-header a {
    color: inherit;
    text-decoration: none;
  }
</style>
