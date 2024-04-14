<script lang="ts">
	// export let old_year: number
	// export let new_year: number
	export let old_year_children: any;
	export let new_year_children: any;
	export let id = '';
</script>

{#each Object.keys(old_year_children) as keys}
	<tr>
		<td>{id + '' + old_year_children[keys].name.split(' ')[0]}</td>
		<td>{old_year_children[keys].name.substring(old_year_children[keys].name.indexOf(' ') + 1)}</td>
		<td>{old_year_children[keys].value.replaceAll(' ', '.')}</td>
		<td>{new_year_children[keys].name}</td>
		<td>{new_year_children[keys].value.replaceAll(' ', '.')}</td>
		<td>{child.value.replaceAll(' ', '.')}</td>
		<td>{new_year_children[index].name}</td>
		<td>{new_year_children[index].value.replaceAll(' ', '.')}</td>
		<td style="text-align:center"
			>{(
				100 -
				(parseFloat(old_year_children[keys].value.replaceAll(' ', '')) /
					parseFloat(new_year_children[keys].value.replaceAll(' ', ''))) *
					100
			).toFixed(2)}%</td
		>
	</tr>
	{#if old_year_children[keys].length !== 0}
		<svelte:self
			id={id + old_year_children[keys].name.split(' ')[0].toString() + '.'}
			old_year_children={old_year_children[keys].child}
			new_year_children={new_year_children[keys].child}
		/>
	{/if}
{/each}
