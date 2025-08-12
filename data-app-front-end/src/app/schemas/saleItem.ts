import {z} from "zod"
import { schemaCreate } from "../../../lib/schemaCreate";


export const saleItemSchema = z.object({
    saleID: z.number({message: "Invalid saleID format"}),
    productID: z.number(),
    qty: z.number().lte(99, "quantity must not exceed 99").gte(0,"quantity must be greater than 0"),
    unitPrice: z.number(),
    lineTotal: z.number().optional()   // line total will be auto calculated
})

export const saleItemArraySchema = z.array(saleItemSchema)

const emptyItem: SaleItem = {
  saleID: 0,
  productID: 0,
  qty: 0,
  unitPrice: 0,
  lineTotal: 0,
};

export const initialSaleItems: SaleItem[] = Array(10).fill(null).map(() => ({...emptyItem}));

export const fieldConfigs = schemaCreate(saleItemSchema)

export type SaleItem = z.infer<typeof saleItemSchema>
export type SaleItemArray = z.infer<typeof saleItemArraySchema>