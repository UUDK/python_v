import logsingleton

logger = logsingleton.LogHub.get_logger()

def bubblesort(data: list) -> list:
    """Sort a list using the bubble sort algorithm."""
    logger.info(f'Starting bubble sort {data}')
    n = len(data)
    logger.debug(f'Starting bubble sort on list of length {n}')
    for i in range(n):
        logger.debug(f'Outer loop iteration {i}')
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                logger.debug(f'Swapping data[{j}]={data[j]} and data[{j+1}]={data[j+1]}')
                data[j], data[j+1] = data[j+1], data[j]
    logger.info(f'Bubble sort completed {data}')
    return data

if __name__ == "__main__":
    logger.info('Program started')
    sample_data = [64, 34, 25, 12, 22, 11, 90]
    sorted_data = bubblesort(sample_data)
    print(f'Sorted data: {sorted_data}')
    logger.info(f'Sorted data: {sorted_data}')
