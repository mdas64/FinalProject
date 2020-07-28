def analyze_spec(spectrogram, freqs, sampling_rate=44100.00, amp_threshold=50):
    '''
    Parameters
    ----------
    spectrogram : numpy.ndarray
        A 2d-array of Fourier coefficients organized by frequencies (rows) and times (columns).

    Returns
    -------
    time_tuples : List[tuple]
        Each tuple contains (time, freqs = []) where freqs is a list of frequencies being played
        at that specified time

    
    time_tuples = []
    
    for freq_num in range(len(spectrogram)):
        for samp_num in range(len(freq_num)):
            if samp_num % 22000:
                freqs = []
                for freq_num in range(len(spectrogram)):
                    if spectrogram[freq_num][samp_num] > amp_threshold:
                        freqs.append(freq_num)
                time_tuples.append( (samp_num / sampling_rate, freqs) )

    return time_tuples

    '''
    time_freq_tuples = []

    for col_ind in range(0,len(spectrogram[0]), 22000):
        myfreqs = []
        print(col_ind)
        for row_ind in range(len(spectrogram)):
            if spectrogram[row_ind, col_ind] > amp_threshold:
                myfreqs.append(freqs[row_ind])
        time_freq_tuples.append( (col_ind / sampling_rate, myfreqs) )
        
    return time_freq_tuples

def get_notes(time_freq_tuples):
    '''
    Parameters
    ----------
    time_tuples :
    
    Returns
    -------
    
    '''
    time_note_tuples = []
    for time, freqs in time_freq_tuples:
        notes = []
        for f in freqs:
            n = freq_to_note(f)
        time_note_tuples.append( (time, notes) )
    
    print(time_note_tuples)
    return time_note_tuples

def freq_to_note(freq):
    '''
    Determines the closet note based on an input frequency.

    Parameters
    ----------
    freq : float

    Returns
    -------
    note_name : String
    '''

    #TODO finish populating notes
    notes = { 130.81 : "C3", 138.59 : "C#3/Db3", 146.83 : "D3", 155.56 : "D#3/Eb3", 440.00 : "A4" }

    note_dis = abs(freq - 440.00)
    note_name = "A4"

    for f in notes.keys():
        new_dis = abs(freq - f)
        if (new_dis < note_dis):
            note_dis = new_dis
            note_name = notes[f]

    return note_name


def display_notes(time_note_tuples):
    '''
    takes the notes and the times they are played and prints out a how long and 
    which notes to play
    '''
    
    for index in range(len(time_note_tuples) - 1):
        time, notes = time_note_tuples[index]
        next_time, next_notes = time_note_tuples[index + 1]
        print("play " + str(notes) + " for " + str(next_time - time) + " seconds.")
    
    
    
    