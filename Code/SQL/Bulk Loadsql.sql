
--- load CSV file into a table.
-- the table was created manually using GUI
-- all nvarchar max
use AGRO_DB_RB
go
BULK INSERT v_Census_AgroLoc
FROM 'MY_PATH_TO_FILE\v_Census (AgroLoc).csv'

WITH
(
   FIRSTROW= 2, -- first row with data to load
   FIELDTERMINATOR = ',',
   ROWTERMINATOR = '\n'
)

--FIRSTROW= 1 will load header as your obs=2
--FIRSTROW indicates the first row with data
--if you have a CSVS will headers, then you need to say FIRSTROW=2




select top 10 * from v_Census_AgroLoc
