import codecs

github = lambda project: f"http://www.github.com/byxor/{project}"
decode = lambda text: codecs.decode(text, "rot_13")
lines = lambda *lines: "\n".join(lines)
commas = lambda *things: ", ".join(things)
