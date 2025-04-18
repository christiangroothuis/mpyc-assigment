from mpyc.runtime import mpc
from mpyc.sectypes import SecureInteger, SecureArray

secnum = mpc.SecInt()


def binary_search(arr: SecureArray, num: SecureInteger):
    n = len(arr)
    i: SecureInteger = secnum(0)
    j: SecureInteger = secnum(n - 1)

    for _ in range(n.bit_length()):
        k = (i + j) // 2
        c = num < arr[k]

        j = mpc.if_else(c, k - 1, j)
        i = mpc.if_else(c, i, k + 1)
        # TODO print values to see if we can derive the branching if values stay the same

    return (i + j) // 2


async def main():
    s = [19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
    x = mpc.seclist(s, secnum)

    async with mpc:
        print(await mpc.output(binary_search(x, secnum(53))))


if __name__ == "__main__":
    mpc.run(main())
