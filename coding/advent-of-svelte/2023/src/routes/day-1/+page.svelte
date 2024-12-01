<script lang="ts">
	import type { PageData } from './$types';
	import type { Child } from './+page';

	const { data }: { data: PageData } = $props();

	const children = $state<Child[]>(data.initialData);

	let child = $state<Child>({
		name: '',
		tally: 0
	});

	function isNice(tally: number): boolean {
		return tally > 0;
	}

	function onSubmit(event: Event): void {
		event.preventDefault();

		children.push({
			name: child.name,
			tally: child.tally
		});

		child.name = '';
		child.tally = 0;
	}
</script>

<main>
	<div>
		{#each children as child}
			<ul>
				<li>
					{child.name} was
					{#if isNice(child.tally)}
						nice
					{:else}
						naughty
					{/if}
					({child.tally})
				</li>
			</ul>
		{/each}
	</div>

	<form onsubmit={onSubmit}>
		<label for="name">Name</label>
		<input bind:value={child.name} id="name" type="text" name="name" required />

		<label for="tally">Tally</label>
		<input bind:value={child.tally} id="tally" type="number" name="tally" required />

		<button type="submit">Add</button>
	</form>
</main>
