class Solution:

    def encode(self, strs: List[str]) -> str:
        sep = "^$#^@^"
        if len(strs) == 0:
            return "emptystring"
        return sep.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "emptystring":
            return []
        return s.split("^$#^@^")
