<script lang="ts">
	export let old_year: number;
	export let new_year: number;
	export let old_year_children: any;
	export let new_year_children: any;
	export let id = '';
	function percentage_increase(a: number, b: number): number {
		// let abs = Math.abs(a - b)
		// let avg = (a+b) / 2
		// return (100 * (Math.abs(a - b)) / ((a+b) / 2)).toFixed(2)
		return (((b - a) / a) * 100).toFixed(2);
	}
	function color_on_percentage(percentage: number): string {
		// console.log(percentage);

		if (Math.floor(percentage) === 0) {
			return 'pico-color-slate-200';
		} else if (percentage > 0 && percentage < 10) {
			return 'pico-color-jade-50';
		} else if (percentage < 0 && percentage > -10) {
			return 'pico-color-pink-50';
		} else if (percentage <= -10000) {
			return 'pico-color-pink-600';
		} else if (percentage <= -1000) {
			return 'pico-color-pink-400';
		} else if (percentage <= -200) {
			return 'pico-color-pink-300';
		} else if (percentage <= -50) {
			return 'pico-color-pink-200';
		} else if (percentage <= -10) {
			return 'pico-color-pink-150';
		} else if (percentage >= 10000) {
			return 'pico-color-jade-600';
		} else if (percentage >= 1000) {
			return 'pico-color-jade-400';
		} else if (percentage >= 200) {
			return 'pico-color-jade-300';
		} else if (percentage >= 50) {
			return 'pico-color-jade-200';
		} else if (percentage >= 10) {
			return 'pico-color-jade-150';
		}
		return 'pico-color-orange-900';
	}

	function calculate_inflation(old_year: number, new_year: number): number {
		let KPI_per_year: Record<number, number> = {
			2024: 414.26, //month of march
			2023: 403.7,
			2022: 371.91,
			2021: 343.19,
			2020: 335.92,
			2019: 334.26,
			2018: 328.4,
			2017: 322.11,
			2016: 316.43,
			2015: 313.35,
			2014: 313.49,
			2013: 314.06,
			2012: 314.2,
			2011: 311.43,
			2010: 303.46,
			2009: 299.66,
			2008: 300.61,
			2007: 290.51
		};
		let years = [2023, 2024].sort((a, b) => {
			return b - a;
		});
		console.log(years);

		// if (new_year > old_year) {
		let old_year_KPI = KPI_per_year[years[0]];
		console.log(old_year_KPI);

		let new_year_KPI = KPI_per_year[years[1]];
		console.log(new_year_KPI);

		let result = ((old_year_KPI - new_year_KPI) / new_year_KPI) * 100;
		// res.innerText = result.toString()
		// realresult.innerText= result
		// res.innerText = Math.round(result*100)/100
		// console.log(Math.round(result*100)/100);

		return result.toFixed(4);
		// }
	}
	function string_to_num(inputString: string) {
		return parseFloat(inputString.replaceAll(' ', ''));
	}
</script>

<table>
	<tr>
		<th>expenditure area</th>
		<th>Old Value</th>
		<th>New Value</th>
		<th>%</th>
		<th>% inflation</th>
	</tr>
	{#each old_year_children as item, index}
		<tr>
			<!-- <td>{index}</td> -->
			{#if item.is_bold}
				<td style="font-weight: bold">{item.name}</td>
			{:else}
				<td>{item.name}</td>
			{/if}
			<td>{item.value.replaceAll(' ', '.')}</td>
			<td>{new_year_children[index].value.replaceAll(' ', '.')}</td>

			<td
				class={color_on_percentage(
					percentage_increase(
						string_to_num(item.value),
						string_to_num(new_year_children[index].value)
					)
				)}
			>
				{percentage_increase(
					string_to_num(item.value),
					string_to_num(new_year_children[index].value)
				)}%
			</td>
			<td
				class={color_on_percentage(
					percentage_increase(
						(string_to_num(item.value) +
							(string_to_num(item.value) / 100) * calculate_inflation(old_year, new_year)),
						string_to_num(new_year_children[index].value)
					)
				)}
			>
				{percentage_increase(
					(string_to_num(item.value) +
						(string_to_num(item.value) / 100) * calculate_inflation(old_year, new_year)),
					string_to_num(new_year_children[index].value)
				)}%
			</td>
		</tr>
		<br />
	{/each}
</table>
