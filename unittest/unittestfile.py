
def test_addnumbers():
    assert sum([7, 12, 9, 5]) == 33, "Result should be 33"



def test_addmorenumbers():
    assert sum((20, 40, 60, 1)) == 99, "Result should be 121"


# Driver code
if __name__ == "__main__":
    test_addnumbers()
    test_addmorenumbers()

    print("Results are: ")