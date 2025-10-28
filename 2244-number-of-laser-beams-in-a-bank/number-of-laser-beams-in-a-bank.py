class Solution:
    # TC: O(n), SC: O(1)
    def numberOfBeams(self, bank: List[str]) -> int:
        beams, prev_devices = 0, 0

        for row in bank:
            curr_devices = row.count("1")
            if curr_devices:
                beams += prev_devices * curr_devices
                prev_devices = curr_devices

        return beams