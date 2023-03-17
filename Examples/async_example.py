import asyncio

async def count_up_to(num: int) -> None:
    """
    An asynchronous function that counts up to a given number and prints each number.

    :param num: The number to count up to.
    :type num: int
    :raises ValueError: If `num` is negative.
    :return: None
    """
    if num < 0:
        raise ValueError("Cannot count up to a negative number")

    for i in range(num):
        print(i)
        await asyncio.sleep(0.1)

async def main() -> None:
    """
    An asynchronous function that calls `count_up_to` with a given number.

    :return: None
    """
    try:
        await count_up_to(10)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    """_summary_
    """
    asyncio.run(main())