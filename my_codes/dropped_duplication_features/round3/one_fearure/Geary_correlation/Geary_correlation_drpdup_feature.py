import codes.drop_duplicatess as dropdup
from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file

# ------------ input files -------------
Geary_90 = '../../../../normalized_features/round3/one_fearure/Geary_correlation/Geary_90_mixed_normalized.tsv'
Geary_80 = '../../../../normalized_features/round3/one_fearure/Geary_correlation/Geary_80_mixed_normalized.tsv'
# ------------ output files -------------
dropdup_90 = 'Geary_90_mixed_dropdup.tsv'
dropdup_80 = 'Geary_80_mixed_dropdup.tsv'
# ---------------------------------------
# drop dups cdhit 90 data
Geary_90_df = get_data_frame_from_tsv_file(Geary_90)
print("before drop 90 cdhit, shape= ", Geary_90_df.shape)
print(Geary_90_df)

dups = dropdup.find_duplicated_columns(Geary_90_df)
df90 = Geary_90_df.drop(dups, axis=1)
print("duplicate cols", dups)

df90 = dropdup.drop_columns_with_same_values(df90)
df90 = dropdup.drop_row_duplicates(df90)
df90.reset_index(drop=True, inplace=True)

print("After drop 90 cdhit, shape= ", df90.shape)

write_data_frame_to_tsv_file(df90, dropdup_90)
# ---------------------------------------
# drop dups cdhit 80 data
Geary_80_df = get_data_frame_from_tsv_file(Geary_80)
print("before drop 80 cdhit, shape= ", Geary_80_df.shape)
print(Geary_80_df)

dups = dropdup.find_duplicated_columns(Geary_80_df)
df80 = Geary_80_df.drop(dups, axis=1)
print("duplicate cols", dups)

df80 = dropdup.drop_columns_with_same_values(df80)
df80 = dropdup.drop_row_duplicates(df80)
df80.reset_index(drop=True, inplace=True)

print("After drop 80 cdhit, shape= ", df80.shape)

write_data_frame_to_tsv_file(df80, dropdup_80)
