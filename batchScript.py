def process_rows_in_batches(input_df, batch_size=100):
    output_data = []

    for i in range(0, len(input_df), batch_size):
        batch = input_df.iloc[i:i + batch_size]
        text_concatenated = ' '.join(batch['text'])
        avg_start = batch['start'].mean()
        avg_end = batch['end'].mean()
        new_id = i
        output_data.append([new_id, text_concatenated, avg_start, avg_end])

    output_df = pd.DataFrame(output_data, columns=['id', 'text', 'start', 'end'])

    return output_df
