import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s',
    filename='app.log',
    )

def bubblesort(data: list) -> list:
    """Sort a list using the bubble sort algorithm."""
    logging.info(f'Starting bubble sort {data}')
    n = len(data)
    logging.debug(f'Starting bubble sort on list of length {n}')
    for i in range(n):
        logging.debug(f'Outer loop iteration {i}')
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                logging.debug(f'Swapping data[{j}]={data[j]} and data[{j+1}]={data[j+1]}')
                data[j], data[j+1] = data[j+1], data[j]
    logging.info(f'Bubble sort completed {data}')
    return data

if __name__ == "__main__":
    logging.info('Program started')
    sample_data = [64, 34, 25, 12, 22, 11, 90]
    sorted_data = bubblesort(sample_data)
    print(f'Sorted data: {sorted_data}')
    logging.info(f'Sorted data: {sorted_data}')
