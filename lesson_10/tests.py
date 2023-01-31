from lesson_10.classwork import check_string

if __name__ == "__main__":
    assert check_string("+375 (29) 299-00-00") is not None
    assert check_string("+375 (2999-00-00") is not None
    assert check_string("+33333333333") is None