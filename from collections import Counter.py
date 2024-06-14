from collections import Counter

def find_min_window(S, T):
    T_counts = Counter(T)  # Character frequencies in T
    window_start = 0
    min_window_len = float('inf')
    min_window = ""

    for window_end, char in enumerate(S):
        if char in T_counts:
            T_counts[char] -= 1  # Decrement count if character is in T

        # All characters in T found in the window
        if all(count >= 0 for count in T_counts.values()):
            while S[window_start] not in T_counts or T_counts[S[window_start]] > 0:
                if T_counts.get(S[window_start], 0) > 0:  # Update count if leaving character is in T
                    T_counts[S[window_start]] += 1
                window_start += 1  # Minimize window size

            current_window_len = window_end - window_start + 1
            if current_window_len < min_window_len:
                min_window_len = current_window_len
                min_window = S[window_start:window_end + 1]

    return min_window if min_window else ""  # Return empty string if no window found
