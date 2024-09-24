# Three electional provinces for the time being
data_matrix = [[12, -11, 52],
               [13, 2, 13],
               [14, 51, -2]]

def printNonNilCandidates(myvector):
    "Simply iterate through the vector and print candidates that got at least one vote"
    for i in range(len(myvector)):
        if myvector[i] > 0:
            print(f"Candidate {i}:\t {myvector[i]}")


def candidateWinsTheProvince(myvector, provincepollsize):
    "Iterate through the vector and return True only if someone has more than half of provincepollsize votes"
    for i in range(len(myvector)):
        if myvector[i] > 0:
            if myvector[i] > provincepollsize/2:
                return True
    return False


# For every line (electional province)

def o_squared_complexity_algorithm():
    "First solution, non-optimized, to the given problem"
    number_of_provinces = len(data_matrix)
    province_vector = [0] * number_of_provinces
    for electional_province in range(number_of_provinces):
        # This should be a rather logical assumption for the working circumstances
        candidate_votes_vector = [0] * 1000
        # This variable is useful to determine
        stop_point = len(data_matrix[electional_province])
        # For every column (point of data at that time)
        for data_point_index in range(stop_point):
            # Agreed upon hypothesis: Valid IDs need to be non-negative
            if data_matrix[electional_province][data_point_index] < 0:
                stop_point = data_point_index
                break
            candidate_votes_vector[data_matrix[electional_province][data_point_index]] += 1
        province_vector[electional_province] = candidatewinstheprovince(candidate_votes_vector, stop_point)
        if province_vector[electional_province]:
            print(f"Someone wins province {electional_province}")
#        else:
#            print(f"Nobody wins province {electional_province}")

o_squared_complexity_algorithm()
