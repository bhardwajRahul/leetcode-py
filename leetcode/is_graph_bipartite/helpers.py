def run_is_bipartite(solution_class: type, graph: list[list[int]]):
    implementation = solution_class()
    return implementation.is_bipartite(graph)


def assert_is_bipartite(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
