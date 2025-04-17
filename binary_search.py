from mpyc.runtime import mpc
from mpyc.sectypes import SecureInteger
from mpyc.seclists import seclist


def binary_search(arr: seclist, num: SecureInteger):
    n = len(arr)
    secnum = mpc.SecInt()
    i: SecureInteger = secnum(0)
    j: SecureInteger = secnum(n - 1)

    for _ in range(n.bit_length()):
        k = (i + j) // 2
        c = num < arr[k]

        j = mpc.if_else(c, k - 1, j)
        i = mpc.if_else(c, i, k + 1)

    return k


async def main():
    s = [19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

    secnum = mpc.SecInt()
    x = list(map(secnum, s))
    x = mpc.seclist(x)

    async with mpc:
        i = binary_search(x, secnum(23))

        print(await mpc.output(i))


if __name__ == "__main__":
    mpc.run(main())
