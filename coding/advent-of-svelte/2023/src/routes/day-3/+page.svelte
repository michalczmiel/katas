<script lang="ts">
	import type { PageData } from './$types';
	import type { Child } from './+page';

	const { data }: { data: PageData } = $props();

	let children = $state<Child[]>(data.initialData);
	let selected = $state<Child[]>([]);

	const maxLoad = 100;
	const currentLoad = $derived(selected.reduce((sum, c) => (sum += c.weight), 0));

	function onAdd(child: Child): void {
		const leftoverLoad = maxLoad - currentLoad;

		if (child.weight > leftoverLoad) {
			alert('Sleigh capacity exceeded');
			return;
		}

		children = children.filter((c) => c.name !== child.name);
		selected.push(child);
	}

	function onRemove(child: Child): void {
		children.push(child);
		selected = selected.filter((c) => c.name !== child.name);
	}
</script>

<main>
	<h1>Jingle Bell Balancer</h1>

	<section>
		<h2>Selected passengers</h2>
		<p>Load {currentLoad.toFixed(2)} / {maxLoad} kg</p>

		{#each selected as child}
			<li>{child.name} <button onclick={() => onRemove(child)}>Remove</button></li>
		{/each}
	</section>

	<div>
		<h2>All children</h2>
		<ul>
			{#each children as child}
				<li>{child.name} {child.weight} kg <button onclick={() => onAdd(child)}>Add</button></li>
			{/each}
		</ul>
	</div>
</main>
