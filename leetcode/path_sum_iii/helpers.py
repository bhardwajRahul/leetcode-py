def run_path_sum(solution_class: type, root_list: list[int | None], target_sum: int):
    from leetcode_py import TreeNode

    root = TreeNode.from_list(root_list)
    implementation = solution_class()
    return implementation.path_sum(root, target_sum)


def assert_path_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
