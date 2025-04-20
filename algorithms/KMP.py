def kmp_search(pattern, text):
    # Build the partial match table (also called failure function)
    def build_lps_array(pattern):
        m = len(pattern)
        lps = [0] * m  # lps[i] = longest proper prefix which is also suffix of pattern[0...i]
        
        # Length of the previous longest prefix & suffix
        length = 0
        i = 1
        
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    # This is tricky. Consider the example: AAACAAAA and i = 7
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    if not pattern or not text:
        return []
    
    n, m = len(text), len(pattern)
    if m > n:
        return []
    
    lps = build_lps_array(pattern)
    
    results = []
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < n:
        # Current characters match, move both pointers
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        # Pattern completely found
        if j == m:
            results.append(i - j)  # Found pattern at index i-j
            j = lps[j - 1]  # Look for the next match
        
        # Mismatch after j matches
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]  # Use the partial match table
            else:
                i += 1
    
    return results