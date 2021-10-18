import codes.drop_duplicatess as dropdup
from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file

# ------------ input files -------------
CKSAAP_90 = '../../../../normalized_features/round3/one_fearure/CKSAAP/CKSAAP_90_mixed_normalized.tsv'
CKSAAP_80 = '../../../../normalized_features/round3/one_fearure/CKSAAP/CKSAAP_80_mixed_normalized.tsv'
# ------------ output files -------------
dropdup_90 = 'CKSAAP_90_mixed_dropdup.tsv'
dropdup_80 = 'CKSAAP_80_mixed_dropdup.tsv'
# ---------------------------------------
# drop dups cdhit 90 data
CKSAAP_90_df = get_data_frame_from_tsv_file(CKSAAP_90)
print("before drop 90 cdhit, shape= ", CKSAAP_90_df.shape)
print(CKSAAP_90_df)

dups = dropdup.find_duplicated_columns(CKSAAP_90_df)
df90 = CKSAAP_90_df.drop(dups, axis=1)
print("duplicate cols", dups)

df90 = dropdup.drop_columns_with_same_values(df90)
df90 = dropdup.drop_row_duplicates(df90)
df90.reset_index(drop=True, inplace=True)

print("After drop 90 cdhit, shape= ", df90.shape)

write_data_frame_to_tsv_file(df90, dropdup_90)
# ---------------------------------------
# drop dups cdhit 80 data
CKSAAP_80_df = get_data_frame_from_tsv_file(CKSAAP_80)
print("before drop 80 cdhit, shape= ", CKSAAP_80_df.shape)
print(CKSAAP_80_df)

dups = dropdup.find_duplicated_columns(CKSAAP_80_df)
df80 = CKSAAP_80_df.drop(dups, axis=1)
print("duplicate cols", dups)

df80 = dropdup.drop_columns_with_same_values(df80)
df80 = dropdup.drop_row_duplicates(df80)
df80.reset_index(drop=True, inplace=True)

print("After drop 80 cdhit, shape= ", df80.shape)

write_data_frame_to_tsv_file(df80, dropdup_80)
