integration_tests = {}

# example test below
def one_plus_one_is_two(done):
    outcome = 1+1
    desired_outcome = 2
    assert outcome == desired_outcome, "1+1 was not equal to two"
    done("one plus one is equal to two")
integration_tests["one plus one is equal to two"] = one_plus_one_is_two