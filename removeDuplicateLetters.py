class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        lastloc = {}
        stack = []
        visited = set()

        # store last occurrence
        for i in range(len(s)):
            lastloc[s[i]] = i

        for i in range(len(s)):

            if s[i] not in visited:

                while (
                    stack
                    and stack[-1] > s[i]
                    and lastloc[stack[-1]] > i
                ):
                    visited.remove(stack.pop())

                stack.append(s[i])
                visited.add(s[i])

        return "".join(stack)
