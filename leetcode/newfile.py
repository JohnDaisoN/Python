import pandas as pd

df = pd.read_csv('data.csv')

sort_order = ['Name', 'Mark', 'Rank']
while True:
    print('Select column to sort by:')
    for i in range(len(sort_order)):
        print(f'{i+1}. {sort_order[i]}')
    user_input = int(input('Enter column number: '))
    if(user_input < 1 or user_input > 3):
        print('Invalid input. Please try again.')
        continue
    else:
        sorted_df = pd.DataFrame(columns=df.columns)

        while not df.empty:
            highest_ranked_index = df[sort_order[user_input-1]].idxmax()
            highest_ranked_row = df.loc[highest_ranked_index]
            sorted_df = sorted_df._append(highest_ranked_row, ignore_index=True)
            df = df.drop(index=highest_ranked_index)
        
        print("Sorted document:")
        print(sorted_df.to_string(index=False))
        sorted_df.to_csv('sorted_data.csv', index=False)
        break
    