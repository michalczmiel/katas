<script lang="ts">
	import { onMount } from 'svelte';

	let dataState = $state<'idle' | 'fetching' | 'error'>('idle');
	let periodInterval = $state(10);
	let ratesAverageWindow = $state<number[]>([]);
	let heartRate = $state(0);
	let average = $state(0);

	async function fetchHeartRate(): Promise<number | null> {
		try {
			const response = await fetch('https://advent.sveltesociety.dev/data/2023/day-four.json');
			const data = await response.json();

			return data.heartRate;
		} catch (error) {
			console.error(error);
			return null;
		}
	}

	async function tick() {
		const current = await fetchHeartRate();
		if (!current) {
			dataState = 'error';
			return;
		}

		dataState = 'fetching';

		heartRate = current;
		if (ratesAverageWindow.length > periodInterval) {
			ratesAverageWindow.shift();
		}

		ratesAverageWindow.push(current);

		average = ratesAverageWindow.reduce((sum, rate) => (sum += rate)) / ratesAverageWindow.length;
	}

	onMount(() => {
		const interval = setInterval(tick, 1000);

		return () => {
			clearInterval(interval);
		};
	});
</script>

<main>
	<h1>Santa's Heart Rate Monitor (SHRM™).</h1>

	{#if dataState === 'idle'}
		<p>Loading live data...</p>
	{:else if dataState === 'fetching'}
		<p>Current: {heartRate} BPM</p>
		<p>Last {periodInterval} seconds average: {average.toFixed(2)}</p>
		<pre>{ratesAverageWindow}</pre>
	{:else}
		<p>Unexpected error happened</p>
	{/if}
</main>
