from Bio import SeqIO


def count_data_by_id(file_name, class_label):
    count = 0
    query = "10|1"
    for seq_record in SeqIO.parse(open(file_name, mode='r'), 'fasta'):

        if query in seq_record.id:
            print(seq_record.seq)
            print(seq_record.id)
            return len(seq_record.seq)


# --------------------------------------------
file_in = 'ACP_100_pos.fasta'
# --------------------------------------------
print(str(count_data_by_id(file_in, "1")))
