import {z} from "zod"
import { schemaCreate } from "../../../lib/schemaCreate";

const today = new Date().toISOString().slice(0,10);

// create validation schema
export const saleSchema = z.object({       // TODO: use z.string.regex for custom format
    saleDate: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, {
        message: "Date must be in YYYY-MM-DD format",
    }),
    receivedDate: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, {
        message: "Date must be in YYYY-MM-DD format",
    }),
    accountID: z.number({message: "Invalid Account ID format"}),
    productLineID: z.number({message: "Invalid Product Line format"}),
    surgeonID: z.number({message: "Invalid Surgeon ID format"}),
    repID: z.number({message: "Invalid RepID format"}),
    rstckLocID: z.number({message:"Invalid Restock Loc ID format"}),
});

export const initialBasicSaleInfo = {
            saleDate: today,
            receivedDate: today,
            accountID: 0,
            productLineID: 0,
            surgeonID: 0,
            repID: 0,
            rstckLocID: 0
}

export type BasicSaleInfo = z.infer<typeof saleSchema>
export const fieldConfigs = schemaCreate(saleSchema)


