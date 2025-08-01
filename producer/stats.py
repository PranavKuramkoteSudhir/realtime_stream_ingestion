from kafka_producer import stats

def print_stats():
    total = stats['successful_events'] + stats['failed_events']
    success_rate = (stats['successful_events'] / total) * 100 if total else 0
    print(f"\nStats: {stats['successful_events']} successes, {stats['failed_events']} fails, {success_rate:.1f}% success")
