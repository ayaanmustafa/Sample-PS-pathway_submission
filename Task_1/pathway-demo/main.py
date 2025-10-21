import pathway as pw

class InputSchema(pw.Schema):
    name: str
    score: int

t = pw.debug.table_from_rows(InputSchema, rows=[("Ayaan", 69), ("Bosh", 10)])

result = t.select(name=t.name, doubled_score=t.score * 2)
pw.debug.compute_and_print(result)
