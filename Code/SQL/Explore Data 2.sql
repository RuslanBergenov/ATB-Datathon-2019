select distinct GEO into #geo_table from censusmat

select * from #geo_table

select 
case
when geo like '%000000000]%' then 'Canada'
when geo like '%PR%' then 'Province'
when geo like '%CAR%' then 'CensusAgriculturalRegion' 
when geo like '%CD%'  then 'CensusDivision' 
when geo like '%CCS%'  then 'CensusConsolidatedSubdivision'
when geo like 'Northwest Territories%' or geo like 'Yukon%' or geo like 'Nunavut%' then 'Territory'
end as Geo_Type,
*
 from #geo_table




