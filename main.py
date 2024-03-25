"""
This code is designed to implement a basic variation of the Gale-Shapley algorithm for solving the stable matching
problem, typically applied in scenarios like matching candidates to hospitals or students to schools based on
preferences.
"""


def k_prefers_h_over_h1(prefer, k, h, h1, N):
    """
    Determines if a candidate (k) prefers one hospital (h) over another (h1).

    Parameters:
        - prefer (list of list of ints): The preference matrix where prefer[0..N-1] are the preferences of hospitals,
          and prefer[N..2N-1] are the preferences of candidates.
        - k (int): The index of the candidate whose preference is being checked.
        - h (int): The index of a hospital to check preference for.
        - h1 (int): The index of the other hospital to compare preference against.
        - N (int): The total number of hospitals (or candidates, since they are equal).

    Returns:
        - bool: True if candidate k prefers hospital h over h1, False otherwise.
    """
    for i in range(N):
        if prefer[k][i] == h:  # h has a higher preference than h1
            return True
        elif prefer[k][i] == h1:  # h1 has a higher preference than h
            return False


def stable_matching(prefer):
    """
    Executes the stable matching algorithm to match N hospitals to N candidates based on mutual preferences.

    Parameters:
        - prefer (list of list of ints): The preference list for all participants. The first N lists represent the
          hospital's preferences over candidates, and the last N lists represent the candidate's preferences over
          hospitals.

    Note:
        - It assumes that there are an equal number of hospitals and candidates.
        - The preference list for each hospital and candidate should be complete and ranked.
    """
    N = len(prefer) // 2

    # Stores the candidates currently matched with the hospital
    # -1 stands for no current match
    k_hospital = [-1 for i in range(N)]

    # Stores the current matching of hospitals
    # If False, than the hospital has no candidate
    free_hospitals = [False for i in range(N)]

    free_count = N

    # While there are hospitals with no candidates
    while free_count > 0:
        h = 0  # Pick the first free hospital
        while h < N:
            if not free_hospitals[h]:  # Free hospital found
                break
            h += 1

        # One by one go to all candidates according to the hospital's preferences
        i = 0
        while i < N and free_hospitals[h] == False:
            k = prefer[h][i]
            i += 1

            if k_hospital[k - N] == -1:  # Candidate has no current match
                k_hospital[k - N] = h  # Candidate has a match with hospital h
                free_hospitals[h] = True  # Hospital h has a candidate
                free_count -= 1
            else:  # Candidate already has a match
                h1 = k_hospital[k - N]
                # If candidate prefers new offer, match the hospital with the candidate and reject old offer
                if k_prefers_h_over_h1(prefer, k, h, h1, N):
                    k_hospital[k - N] = h
                    free_hospitals[h] = True
                    free_hospitals[h1] = False  # The previous hospital h1 is now free

    print("Hospital", "Candidate")
    for i in range(N):
        print(i, "\t", k_hospital[i] + N)


if __name__ == '__main__':
    # Example preferences: Hospitals (0, 1, 2) and Candidates (3, 4, 5)
    prefer = [
        [3, 5, 4],  # Hospital 0's preferences over candidates
        [3, 4, 5],  # Hospital 1's preferences
        [3, 5, 4],  # Hospital 2's preferences
        [1, 2, 0],  # Candidate 3's preferences over hospitals
        [2, 1, 0],  # Candidate 4's preferences
        [2, 0, 1]   # Candidate 5's preferences
    ]

    stable_matching(prefer)

