def love_meet(bob, alice):
    return set(bob) & set(alice)


def affair_meet(bob, alice, silvester):
    for i in bob:
        for i in alice:
            alice.remove(i)
    return set(silvester) & set(alice)