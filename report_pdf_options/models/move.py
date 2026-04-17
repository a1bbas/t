from odoo import models, fields, api,_
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = "account.move"

    old_name = fields.Char(string="Previous Invoice Number", copy=False)

    def action_reset_draft_keep_number(self):
        """Custom button to reset invoice to draft but preserve number."""
        for move in self:
            if move.state != 'posted':
                raise UserError("Only posted invoices can be reset to draft.")

            if move.name and move.name != '/':
                move.old_name = move.name  # Store current invoice number

            # Reset state to draft
            move.button_draft()

            # Optional: Add a message in chatter
            move.message_post(
                body="Invoice was reset to draft, original number '%s' preserved."
                     % move.old_name
            )

    def post(self):
        """Reuse old number if available when posting again."""
        for move in self:
            if move.old_name:
                # Check for uniqueness
                existing = self.env['account.move'].search([
                    ('name', '=', move.old_name),
                    ('id', '!=', move.id),
                    ('state', '=', 'posted')
                ])
                if existing:
                    raise UserError(
                        "Cannot reuse invoice number '%s' because it is already used."
                        % move.old_name
                    )
                move.name = move.old_name
                move.old_name = False
        return super(AccountMove, self).post()
