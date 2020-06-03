def activity_number_testing(sequence_short,sequence_long,hmm_short,hmm_long,n_act):
    correct_short=0
    wrong_short=0
    correct_long=0
    wrong_long=0
    pcs=[]
    pws=[]
    pcl=[]
    pwl=[]

    for xi in sequence_short:
        seq_test=xi[:n_act]
        prob_short, _ = hmm_short.score_samples(seq_test)
        prob_long, _ = hmm_long.score_samples(seq_test)

        if prob_short>prob_long:
            correct_short+=1
            pcs.append(prob_short-prob_long)
        else:
            wrong_short+=1
            pws.append(prob_long-prob_short)

    for xi in sequence_long:
        seq_test=xi[:n_act]
        prob_short, _ = hmm_short.score_samples(seq_test)
        prob_long, _ = hmm_long.score_samples(seq_test)

        if prob_short<prob_long:
            correct_long+=1
            pcl.append(prob_long-prob_short)
        else:
            wrong_long+=1
            pwl.append(prob_short-prob_long)

    return correct_long,correct_short,wrong_long,wrong_short


def first_week_number_testing(sequence_short,sequence_long,hmm_short,hmm_long):
    correct_short=0
    wrong_short=0
    correct_long=0
    wrong_long=0
    pcs=[]
    pws=[]
    pcl=[]
    pwl=[]

    for xi in sequence_short:
        seq_test=xi[:]
        prob_short, _ = hmm_short.score_samples(seq_test)
        prob_long, _ = hmm_long.score_samples(seq_test)

        if prob_short>prob_long:
            correct_short+=1
            pcs.append(prob_short-prob_long)
        else:
            wrong_short+=1
            pws.append(prob_long-prob_short)

    for xi in sequence_long:
        seq_test=xi[:]
        prob_short, _ = hmm_short.score_samples(seq_test)
        prob_long, _ = hmm_long.score_samples(seq_test)

        if prob_short<prob_long:
            correct_long+=1
            pcl.append(prob_long-prob_short)
        else:
            wrong_long+=1
            pwl.append(prob_short-prob_long)

    return correct_long,correct_short,wrong_long,wrong_short