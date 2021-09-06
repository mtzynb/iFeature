from Bio import SeqIO


def get_seq_by_class_label(file_name, class_label, output_file):
    query = "|" + class_label
    result = []
    for seq_record in SeqIO.parse(open(file_name, mode='r'), 'fasta'):
        if query in seq_record.id:
            result.append(seq_record)

    SeqIO.write(result, output_file, "fasta")

    return result


def split_all_data():
    get_seq_by_class_label("../../../data/ACP_dataset/fasta/ACP-Mixed-40.fasta", "1", "ACP_40_pos.fasta")
    get_seq_by_class_label("../../../data/ACP_dataset/fasta/ACP-Mixed-40.fasta", "0", "ACP_40_neg.fasta")

    get_seq_by_class_label("../../../data/ACP_dataset/fasta/ACP-Mixed-50.fasta", "1", "ACP_50_pos.fasta")
    get_seq_by_class_label("../../../data/ACP_dataset/fasta/ACP-Mixed-50.fasta", "0", "ACP_50_neg.fasta")

    get_seq_by_class_label("../../../data/ACP_dataset/fasta/ACP-Mixed-60.fasta", "1", "ACP_60_pos.fasta")
    get_seq_by_class_label("../../../data/ACP_dataset/fasta/ACP-Mixed-60.fasta", "0", "ACP_60_neg.fasta")

    get_seq_by_class_label("../../../data/ACP_dataset/fasta/ACP-Mixed-70.fasta", "1", "ACP_70_pos.fasta")
    get_seq_by_class_label("../../../data/ACP_dataset/fasta/ACP-Mixed-70.fasta", "0", "ACP_70_neg.fasta")

    get_seq_by_class_label("../../../data/ACP_dataset/fasta/ACP-Mixed-80.fasta", "1", "ACP_80_pos.fasta")
    get_seq_by_class_label("../../../data/ACP_dataset/fasta/ACP-Mixed-80.fasta", "0", "ACP_80_neg.fasta")

    get_seq_by_class_label("../../../data/ACP_dataset/fasta/ACP-Mixed-90.fasta", "1", "ACP_90_pos.fasta")
    get_seq_by_class_label("../../../data/ACP_dataset/fasta/ACP-Mixed-90.fasta", "0", "ACP_90_neg.fasta")

    get_seq_by_class_label("../../../data/ACP_dataset/fasta/ACP-Mixed-100.fasta", "1", "ACP_100_pos.fasta")
    get_seq_by_class_label("../../../data/ACP_dataset/fasta/ACP-Mixed-100.fasta", "0", "ACP_100_neg.fasta")


split_all_data()
