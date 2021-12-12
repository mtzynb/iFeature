from codes.label_creator import get_label_data_from_tsv_file

# ------------ input files -------------

combined_90 = 'QSOrder_CKSAAP_combined_90_mixed_normalized_drpdup.tsv'

# ------------ output files -------------
label_90 = 'QSOrder_CKSAAP_combined_90_mixed_normalized_drpdup_label.tsv'
# ---------------------------------------
# # drop dups cdhit 90  data
get_label_data_from_tsv_file(combined_90, label_90)
