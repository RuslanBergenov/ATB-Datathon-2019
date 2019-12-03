select top 100 * from [dbo].[CensusMat]



select 
top 10
*
from 
[dbo].[CensusMat]
where 
indicator = 'Pigs'



select 
indicator,
indicatorlevel,
sum (Value)
from 
[dbo].[CensusMat]
where 
indicator = 'Pigs'
group by 
indicator,
indicatorlevel



select 
indicator,
indicatorlevel,
sum (Value)
from 
[dbo].[CensusMat]
where 
indicator = 'Bees'
group by 
indicator,
indicatorlevel