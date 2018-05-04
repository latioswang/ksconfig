foo = importProto("bar/foo.proto")
bar = importProto("bar/bar.proto")

exportIfLast(foo.Config(
    name="123123",
    types=[1, 2, 3]
))