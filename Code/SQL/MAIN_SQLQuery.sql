select distinct
-- get geo type based on geo name
case
when geo like '%#[000000000#]%' {escape '#'}  then 'Canada'
when geo like '%#[PR%' {escape '#'}  then 'Province'
when geo like '%#[CAR%' {escape '#'}  then 'CensusAgriculturalRegion'
when geo like '%#[CD%'  {escape '#'}  then 'CensusDivision'
when geo like '%#[CCS%' {escape '#'}   then 'CensusConsolidatedSubdivision'
when geo like 'Northwest Territories%' or geo like 'Yukon%' or geo like 'Nunavut%' then 'Territory'
end as Geo_Type,

GEO,

-- remove all characters after ' ['
LEFT(GEO, CHARINDEX(' [', GEO) - 1) as GEO1,
REPLACE(CONCAT(Indicator,'_',IndicatorLevel,'_',[Unit of Measure]), ' ', '') as Parameter,
sum (Value) as SumValue

from [dbo].[censusmat]

where SourceTable in (32100426, 32100432, 32100446 )

group by

(case
when geo like '%#[000000000#]%' {escape '#'}  then 'Canada'
when geo like '%#[PR%' {escape '#'}  then 'Province'
when geo like '%#[CAR%' {escape '#'}  then 'CensusAgriculturalRegion'
when geo like '%#[CD%'  {escape '#'}  then 'CensusDivision'
when geo like '%#[CCS%' {escape '#'}   then 'CensusConsolidatedSubdivision'
when geo like 'Northwest Territories%' or geo like 'Yukon%' or geo like 'Nunavut%' then 'Territory'
end),

GEO,
LEFT(GEO, CHARINDEX(' [', GEO) - 1) ,
REPLACE(CONCAT(Indicator,'_',IndicatorLevel,'_',[Unit of Measure]), ' ', '')













select distinct
-- get geo type based on geo name
case
when geo like '%#[000000000#]%' {escape '#'}  then 'Canada'
when geo like '%#[PR%' {escape '#'}  then 'Province'
when geo like '%#[CAR%' {escape '#'}  then 'CensusAgriculturalRegion'
when geo like '%#[CD%'  {escape '#'}  then 'CensusDivision'
when geo like '%#[CCS%' {escape '#'}   then 'CensusConsolidatedSubdivision'
when geo like 'Northwest Territories%' or geo like 'Yukon%' or geo like 'Nunavut%' then 'Territory'
end as Geo_Type,


-- remove all characters after ' ['
LEFT(GEO, CHARINDEX(' [', GEO) - 1) as GEO1,
REPLACE(CONCAT(Indicator,'_',IndicatorLevel,'_',[Unit of Measure]), ' ', '') as Parameter,
sum (Value) as SumValue

from [dbo].[censusmat]

where SourceTable in (32100426, 32100432, 32100446 )

group by

(case
when geo like '%#[000000000#]%' {escape '#'}  then 'Canada'
when geo like '%#[PR%' {escape '#'}  then 'Province'
when geo like '%#[CAR%' {escape '#'}  then 'CensusAgriculturalRegion'
when geo like '%#[CD%'  {escape '#'}  then 'CensusDivision'
when geo like '%#[CCS%' {escape '#'}   then 'CensusConsolidatedSubdivision'
when geo like 'Northwest Territories%' or geo like 'Yukon%' or geo like 'Nunavut%' then 'Territory'
end),

LEFT(GEO, CHARINDEX(' [', GEO) - 1) ,
REPLACE(CONCAT(Indicator,'_',IndicatorLevel,'_',[Unit of Measure]), ' ', '')