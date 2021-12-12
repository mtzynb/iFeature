import codes.drop_duplicatess as dropdup
from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file

# ------------ input files -------------
combined_normalized_90 = 'DDE_APseudoAAC_combined_90_mixed_normalized.csv'
# ------------ output files -------------
dropdup_90 = 'DDE_APseudoAAC_combined_90_mixed_normalized_drpdup.tsv'
# ---------------------------------------
# drop dups cdhit 90 data
combined_normalized_90_df = get_data_frame_from_tsv_file(combined_normalized_90)
print("before drop 90 cdhit, shape= ", combined_normalized_90_df.shape)

dups = dropdup.find_duplicated_columns(combined_normalized_90_df)
df90 = combined_normalized_90_df.drop(dups, axis=1)
print("duplicate cols", dups)

df90 = dropdup.drop_columns_with_same_values(df90)
df90 = dropdup.drop_row_duplicates(df90)
df90.reset_index(drop=True, inplace=True)

print("After drop 90 cdhit, shape= ", df90.shape)  # (940, 429) =>

write_data_frame_to_tsv_file(df90, dropdup_90)
